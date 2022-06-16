var additemID = 0;
function addservice(item){
    additemID += 1;
    var selecteditem = document.createElement('div');
    selecteditem.classList.add('serviceimg');
    selecteditem.setAttribute('id', additemID);
    var img = document.createElement('img');
    img.setAttribute('src', item.children[0].currentSrc);
    var cardtext = document.createElement('div');
    cardtext.innerText = item.children[1].innerText;
    var label = document.createElement('div');
    label.innerText = item.children[2].children[0].innerText;
    var select = document.createElement('span');
    select.innerText = item.children[2].children[1].value;
    label.append(select);
    var delBtn = document.createElement('button');
    delBtn.innerText = 'Delete';
    delBtn.setAttribute('onclick', 'del(+additemID+)');
    var serviceitems = document.getElementById('cardtext');
    selecteditem.append(img);
    selecteditem.append(label);
    selecteditem.append(cardtext);
    selecteditem.append(delBtn);
    serviceitems.append(selecteditem);

}

function del(item){
    document.getElementById(item).remove();
}