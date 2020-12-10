function alternarVista() {
    var contrasenaNueva = document.getElementById('thePassword');
    if (contrasenaNueva.type === 'password') {
      contrasenaNueva.type = 'text';
    } else {
      contrasenaNueva.type = 'password';
    }
  
    var repetirContrasena = document.getElementById('repPassword');
    if (repetirContrasena.type === 'password') {
      repetirContrasena.type = 'text';
    } else {
      repetirContrasena.type = 'password';
    }
  }
  
  function mouseAbajo(ver) {
    var contrasenaNueva_1 = document.getElementById('thePassword');
    if (ver) {
      contrasenaNueva_1.type = 'text';
    } else {
      contrasenaNueva_1.type = 'password';
    }
  }
  
  function mouseArriba() {
    var contrasenaNueva_2 = document.getElementById('thePassword');
    contrasenaNueva_2.type = 'password';
  }
  