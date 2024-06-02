23:41:09 UTC
$(ls -R | grep ':$' | sed -e 's/:$//' -e 's/[^-][^\/]*\//──/g' -e 's/─/├/' -e '$s/├/└/')

{COMMAND}
