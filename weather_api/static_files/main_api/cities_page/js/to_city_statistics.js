function to_city_choose_params(city_id){
    const full_url = location.protocol + '//' + location.host + location.pathname;
    const redirect_url = full_url + `city/${city_id}/choose_params/`;
    window.location.href = redirect_url;
}

function toCountries() {
    window.history.back();
}