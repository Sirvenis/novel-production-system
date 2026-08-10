import subprocess, sys, pathlib
profile=sys.argv[1]; prompt=pathlib.Path(sys.argv[2]).read_text(); out=pathlib.Path(sys.argv[3]); err=pathlib.Path(sys.argv[4])
cmd=["hermes","--profile",profile,"chat","-q",prompt]
proc=subprocess.run(cmd,text=True,capture_output=True,timeout=1200)
out.write_text(proc.stdout)
err.write_text(proc.stderr)
raise SystemExit(proc.returncode)
