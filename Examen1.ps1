Write-host "Hugo"
Get-Service | Where-Object {$_.Status -eq 'Running'} | Select-Object name > serveis.html
Write-Information serveis.html > serveis.txt