#!/usr/bin/env python3
"""Deterministic validator for future Writer candidate submissions.
Design-phase utility: validates local text files only; does not call models.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

WORD_RE=re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?")
NAME_RE=re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b")

KNOWN_NAMES={
    'Mara','Venn','Mara Venn','Tobin','Tobin Venn','Eda','Kroll','Eda Kroll','Jon','Vale','Jon Vale','Sel','Grayhaven',
    'Jun','Park','Jun Park','Ari','Ari Park','Noma','Saye','Noma Saye','Pip','Pip-9','Larkspur','Sunrise Noodles'
}

def prose_part(text):
    return text.split('SCENE',1)[1] if 'SCENE' in text else text

def count_words(text):
    return len(WORD_RE.findall(prose_part(text)))

def marker_order(text, markers):
    positions=[]
    for m in markers:
        idx=text.find(m)
        if idx<0:
            return False, f"missing marker: {m}"
        positions.append(idx)
    if positions != sorted(positions):
        return False, "markers out of order"
    # duplicates
    for m in markers:
        if text.count(m)!=1:
            return False, f"marker count not one: {m} count={text.count(m)}"
    return True, "ok"

def literal_check(text, literals):
    lower=text.lower()
    missing=[]
    for lit in literals:
        if lit.lower() not in lower:
            missing.append(lit)
    return missing

def forbidden_check(text, forbidden):
    lower=text.lower()
    hits=[]
    for item in forbidden:
        if item.lower() in lower:
            hits.append(item)
    return hits

def validate(packet, submission):
    gt=json.loads(Path(packet).read_text())
    text=Path(submission).read_text()
    words=count_words(text)
    order_ok, order_msg=marker_order(text, gt['required_markers'])
    missing=literal_check(text, gt.get('hard_literals', []))
    forbidden=forbidden_check(text, gt.get('forbidden_resolution', []))
    result={
        'packet_id': gt['packet_id'],
        'submission': str(submission),
        'word_count': words,
        'minimum_words': gt['minimum_words'],
        'word_count_pass': words >= gt['minimum_words'],
        'marker_order_pass': order_ok,
        'marker_order_message': order_msg,
        'missing_hard_literals': missing,
        'hard_literal_pass': not missing,
        'forbidden_resolution_hits': forbidden,
        'forbidden_resolution_pass': not forbidden,
    }
    result['deterministic_eligible']=all([
        result['word_count_pass'], result['marker_order_pass'], result['hard_literal_pass'], result['forbidden_resolution_pass']
    ])
    result['category']='ELIGIBLE' if result['deterministic_eligible'] else 'D_DETERMINISTIC_DISQUALIFIER'
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ground-truth', required=True)
    ap.add_argument('--submission', required=True)
    ap.add_argument('--json-out')
    args=ap.parse_args()
    res=validate(args.ground_truth, args.submission)
    out=json.dumps(res, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(out + '\n')
    print(out)
    return 0 if res['deterministic_eligible'] else 2
if __name__=='__main__':
    raise SystemExit(main())
