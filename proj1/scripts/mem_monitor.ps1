$myprogram=$args[0]
$mypid=(tasklist /FI "IMAGENAME eq $myprogram" /FO CSV).Split(",")[6].Split('"')[1]
While ($true) {
    (wmic process where processid=$mypid get WorkingSetSize).Split([Environment]::NewLine)[2]
    Start-Sleep -Seconds $args[1]
}
