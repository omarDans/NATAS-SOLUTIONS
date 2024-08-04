<?php
    $text = readline("Enter Cookie: ");
    $data = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    $key = "";
    $encoded = json_encode($data);
    $decoded_text = base64_decode($text);
    for($i=0;$i<strlen($decoded_text);$i++) {
        $key .= $decoded_text[$i] ^ $encoded[$i % strlen($encoded)];
    }
    $key = substr($key, 0, 4);
    echo "key found!: " . $key;
    echo "\nCreating cookie...";
    $data2 = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
    $outText = "";
    $data2_encoded = json_encode($data2);
    for($j=0;$j<strlen($data2_encoded);$j++) {
        $outText .= $data2_encoded[$j] ^ $key[$j % strlen($key)];
    }
    $outText = base64_encode($outText);
    echo "\nCustom Cookie: " . $outText;
?>