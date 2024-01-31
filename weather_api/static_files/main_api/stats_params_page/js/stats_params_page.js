function get_all_checked() {
    let checkBoxValues = document.getElementsByName('stats_checkbox');
    let checkedValues = [];
    for (let value of checkBoxValues){
        if (value.checked){
            checkedValues.push(value.value);
        }
    }
    return checkedValues;
}

function calc_func() {
    const checkedValues = get_all_checked();

    console.log(checkedValues);
}