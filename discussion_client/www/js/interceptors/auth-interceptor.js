DiscussApp.factory('AuthInterceptor', function($injector){

	var AuthInterceptor = {

		request: function(config){
			var AuthService = AuthService || $injector.get('AuthService');
			var token = AuthService.token;

			if(token){
				config.headers['Authorization'] = 'JWT ' + token;
			}
			return config;
		},

		responseError: function(response){
			if(response.status === 403){
				window.location.href = '/';
			}
			return response;
		}
	};

	return AuthInterceptor
});