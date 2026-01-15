[string]$nombre= Read-Host "Introduzca tu nombre"
[int]$veces= Read-Host "¿Cuántas veces quieres escribirlo?"
$salto= "`n"
Write-Host (($nombre+$salto)*$veces) 