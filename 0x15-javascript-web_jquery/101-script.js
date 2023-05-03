document.addEventListener('DOMContentLoaded', (e) => {
  const addItem = $('DIV#add_item');
  const removeItem = $('DIV#remove_item');
  const clearItems = $('DIV#clear_list');
  const List = $('UL.my_list');

  addItem.on('click', function (e) {
    List.append('<li>Item</li>');
    e.preventDefault();
  });
  removeItem.on('click', function (e) {
    List.children().last().remove();
    e.preventDefault();
  });
  clearItems.on('click', function (e) {
    List.children().remove();
    e.preventDefault();
  });
  e.preventDefault();
});
