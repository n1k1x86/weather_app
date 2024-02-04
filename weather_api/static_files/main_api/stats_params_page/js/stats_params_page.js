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
    if (!checkedValues.length){
        const current_url = window.location.href.replace('/choose_params/', '/no_chosen_data/');
        window.location.href = current_url;
    } else {
    const current_url = window.location.href.replace('/choose_params/', '/built_statistics/');
    const get_params = '?param=' + checkedValues.join('&param=');
    window.location.href = current_url + get_params;
    }
}

function toCities() {
    window.history.back();
}
