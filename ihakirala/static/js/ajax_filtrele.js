function kategori_(kategori) {
    document.getElementById('search-input').value = '';
    let param = 'Kategori='+ kategori;
    send_request(param);
  }

  function search_(sort_type) {
    document.getElementById('search-input').value = '';
    let param = 'flight_time='+ sort_type;
    send_request(param);
  }

  function find_location() {
    let location = document.getElementById('search-input').value;
    let param = 'search='+ location;
    send_request(param);
  }

  function send_request(param) {
    $.ajax({
      method: 'GET',
      url: 'search/?' + param,
      success: function(result) {
        update_table(result);
      },
      error: function() {
        console.log('error');
      }
    });
  }

  function update_table(data) {
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
      elem = data[key];

      row =
        '<tr><td><p class=' + '"fw-bold d-block fs-7">' + elem['marka'] + '</p></td>'
        + '<td><p class=' + '"fw-bold d-block fs-7">' + elem['model'] + '</p></td>'
        + '<td><p class=' + '"fw-bold d-block fs-7 text-center">' + elem['weight'] + ' Kg.</p></td>'
        + '<td><p class=' + '"fw-bold d-block fs-7 text-center">' + elem['flight_time'] + ' Saat</p></td>'
        + '<td><p class=' + '"fw-bold d-block fs-7">' + elem['kategori'] + '</p></td>' + '</tr>'
      ;

      all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
  }
