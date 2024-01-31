function to_city_redirect(country_id) {
    const full_url = location.protocol + '//' + location.host + location.pathname;
    const redirect_url = full_url + `country/${country_id}/`;
    window.location.href = redirect_url;
}