+++
key = "hello"
work_area = "editor"
editable = ["main.py"]

[check]
type = "python"
script = "check.py"
timeout_secs = 15

[run]
python = "main.py"
+++
# Greet someone

## Concept

A program can join two pieces of text into one.

## Example

`"Good " + "day"` makes `"Good day"`.

## Try it

Set `greeting` to `"Hello, "` followed by `name`.

## Hint

Join them with `+`.

## Check

`greeting` must be `"Hello, Sam"`.
