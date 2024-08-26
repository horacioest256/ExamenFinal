function incrementarNumero()
{
    valorNumero = document.getElementById('numeroEditar')
    numeroIncrementado = Number(valorNumero.innerHTML) + 1
    valorNumero.innerHTML = String(numeroIncrementado)
}

function decrementarNumero()
{
    valorNumero = document.getElementById('numeroEditar')
    numeroIncrementado = Number(valorNumero.innerHTML) - 1
    valorNumero.innerHTML = String(numeroIncrementado)
}

function cargarNumero()
{
    valorNumero = document.getElementById('valorNumero')
    obj1 = document.getElementById('numeroSelect')
    obj1.value = String(valorNumero.value)
}

function agregarNumero()
{
    obj1 = document.getElementById('numeroSelect')
    if(!isNaN(Number(obj1.value)))
    {
        listaNumeros = document.getElementById('listaNumeros')
        listaNumeros.innerHTML += `<li class='numInfo'>${obj1.value}</li>`
    }
    else
    {
        alert('NO HA SELECCIONADO UN NUMERO VALIDO')
    }
    

}