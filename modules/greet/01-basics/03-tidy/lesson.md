+++
key = "tidy"
work_area = "terminal"
project = true
editable = ["notes.txt", "old.txt"]

[check]
type = "command"
run = ["sh", "-c", "exec sh \"$LESSON_DIR/check.sh\""]
+++
# Tidy up

## Concept

A finished folder keeps only what it needs.

## Example

An old draft can go once the notes are written.

## Try it

Write `done` in `notes.txt` and delete `old.txt`.

## Check

`notes.txt` holds `done` and `old.txt` is gone.
