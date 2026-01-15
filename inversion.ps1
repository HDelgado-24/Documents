[float]$inv= Read-Host "Introduzca cuánto va a invertir"
[float]$int= Read-Host "Introduzca el interés anual"
[float]$ano= Read-Host "Introduzca el número de años"
[float]$cap= $inv * [math]::pow(1+($int/100),$ano)
Write-Host $cap