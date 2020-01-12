var pornim = prompt("Pornim aplicatia? y/n");
var evidenta=[];

function Adauga(numeNou)
{
    var numeNou = prompt('Ce nume doresti sa adaugi?');
    evidenta.push(numeNou);
}

/*
https://love2dev.com/blog/javascript-remove-from-array/
*/
function Elimina()
{
    var numeElim = prompt('Ce nume doresti sa stergi?');
    var index = evidenta.indexOf(numeElim);
    if (index !== -1)
    {
        evidenta.splice(index,1);
    }
}

function Afiseaza() {
  console.log(evidenta);
}

var actiune = '';


if (pornim === 'y')
{
    while(actiune !== 'quit')
    {
        actiune = prompt('Selecteaza o actiune: add, remove, display sau quit.');
        if (actiune === 'add')
        {
            Adauga();
        }
        else if (actiune === 'remove')
        {
            Elimina();
        }
        else if (actiune === 'display')
        {
            Afiseaza();
        }

    }
}
