document.addEventListener('DOMContentLoaded', function() {
    // Side Nav initialisation  
    let sideNav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNav);

    // Date Picker initialisation
    let datePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datePicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}

    
    });

    // Select initialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
});