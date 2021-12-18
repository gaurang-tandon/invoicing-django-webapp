var item_count = 0 ;
var total_amt = 0;
document.getElementById('item_count').setAttribute('value',(item_count+1)) ;
console.log("Hello World!!!q!");
var my_html = document.getElementById('item_row').innerHTML;
var table = document.getElementById('items_table');
function addItemsRow(){
  console.log("AddItem Check");
    var item_quantity = (document.getElementById("item_quantity").value);
    var item_rate = (document.getElementById("item_rate").value);
    console.log(item_quantity , item_rate);
    if(item_quantity == "" || item_rate == ""){
      alert("Fill All Fields Of Prior Item First");
      return null;
    }
    document.getElementById('item_id').setAttribute('Readonly', 'true');
    document.getElementById('item_rate').setAttribute('Readonly', 'true');
    document.getElementById('item_quantity').setAttribute('Readonly', 'true');
    document.getElementById('amount').setAttribute('Readonly', 'true');
    document.getElementById('item_id').setAttribute('name', ('item_id['+item_count+']'));
    document.getElementById('item_id').setAttribute('id', ('item_id['+item_count+']'));
    document.getElementById('item_quantity').setAttribute('name', ('item_quantity['+item_count+']'));
    document.getElementById('item_quantity').setAttribute('id', ('item_quantity['+item_count+']'));
    document.getElementById('item_rate').setAttribute('name', ('item_rate['+item_count+']'));
    document.getElementById('item_rate').setAttribute('id', ('item_rate['+item_count+']'));
    document.getElementById('amount').setAttribute('name', ('amount['+item_count+']'));
    document.getElementById('amount').setAttribute('id', ('amount['+item_count+']'));
    item_count++ ;
    document.getElementById('item_count').setAttribute('value',(item_count+1)) ;
    let tr = document.createElement("tr");
    table.appendChild(tr);
    tr.innerHTML = my_html;
    console.log(item_count);
}
function q_change(){
  var item_quantity = Number(document.getElementById('item_quantity').value);
  var item_rate = Number(document.getElementById('item_rate').value);
  if(item_quantity != 0 && item_rate != 0){
    document.getElementById('amount').value = item_quantity*item_rate;
    total_amt += (item_quantity*item_rate);
    console.log(total_amt);
    document.getElementById('bill_amt').value = total_amt;
  }
  console.log("Item-Q = " + item_quantity + ", Item-R = " + item_rate);
}