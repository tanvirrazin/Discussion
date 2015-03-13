DiscussApp.factory('AuthService', ['Resources', '$http', function(Resources, $http){

	var session;
	var service = {
		token: '',
		login: function(credentials, callback){
			$http({
				method: 'POST',
				url: Resources.SERVER_DOMAIN + '/api/auth/login/',
				data: credentials
			})
			.success(function(response, status){
				if(response.token){
					service.token = response.token;
				}
				if(status == 200){
					var response_data = {
						success: true,
						result: response
					}
				} else {
					var response_data = {
						success: false,
						result: response
					}
				}
				callback(response_data);
			})
			.error(function(response){
				var response_data = {
					success: false,
					result: response
				}
				callback(response_data);
			});
		},

		logout: function(){
			service.token = '';
		},

		signup: function(){

		},

		isLoggedIn: function(){

		},

		initializeSession: function(callback){

		},

		getSession: function(){
			// if(session)
			// 	return session;
			// else
			// 	initializeSession(function(session_data){
			// 		return session_data;
			// 	});
		}
	};

	return service;
}]);