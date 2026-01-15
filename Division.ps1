[int]$n= Read-Host "Inserte un número"
[int]$m= Read-Host "Inserte otro número"
[float]$c= $n/$m
[float]$r= $n%$m
Write-Host La división resultante de dividir $n entre $m da un cociente $c y un resto $r