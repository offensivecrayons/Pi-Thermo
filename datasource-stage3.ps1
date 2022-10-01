
# sub this for IP of the pi
$ipaddress = "10.6.50.203"

#pull the web page and store it as $request
$request = Invoke-WebRequest -uri $ipaddress -UseBasicParsing

$stage1= Select-String -InputObject $request -Pattern "Temp:"| Out-String
#this will select "Temp: *****" from the webrequest

[int]$stage2=$stage1.replace("Temp:","")
#removes the "Temp:" string

[decimal]$stage3 = $stage2 / 1000

write-host $stage3