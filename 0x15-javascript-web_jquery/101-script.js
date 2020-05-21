function addElement () { $('.my_list').append('<li>Item</li>'); }
function removeElement () { $('.my_list li').last().remove(); }
function clearList () { $('.my_list').empty(); }

$(document).ready(function () {
  $('DIV#add_item').click(addElement);
  $('DIV#remove_item').click(removeElement);
  $('DIV#clear_list').click(clearList);
});
