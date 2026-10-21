cd "$WORK_DIR" || exit 1
[ "$(cat notes.txt)" = "done" ] || { echo "notes.txt must hold done"; exit 1; }
[ ! -e old.txt ] || { echo "delete old.txt"; exit 1; }
