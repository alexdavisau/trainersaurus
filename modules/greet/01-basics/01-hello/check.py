import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.environ["MODULE_DIR"] + "/_lib")
import greetkit  # noqa: E402

scope = {}
exec(open(os.path.join(os.environ["WORK_DIR"], "main.py")).read(), scope)
greetkit.expect(scope.get("greeting") == "Hello, Sam", 'set greeting to "Hello, Sam"')
