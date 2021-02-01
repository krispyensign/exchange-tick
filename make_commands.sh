make --always-make --dry-run \
 | grep -wE 'gcc|g++|clang|clang++' \
 | grep -w '\-c' \
 | jq -nR '[inputs|{directory:".", command:., file: match(" [^ ]+$").string[1:]}]' \
 > compile_commands.json