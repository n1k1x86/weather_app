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
    const current_url = window.location.href;
     $.ajax({
        type: "POST",
        url: current_url + 'built_statistics/',
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        data: {
            "checkedValues": checkedValues,
        },
        dataType: "json",
        success: function (data) {
        },
        failure: function () {
        }
    });
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }