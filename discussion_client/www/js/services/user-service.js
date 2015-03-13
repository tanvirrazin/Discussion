DiscussApp.factory('UserService', ['Resources', '$http', function(Resources, $http){

	var service = {

		getFriends: function(callback){
			$http({
				method: 'GET',
				url: Resources.SERVER_DOMAIN + '/api/friends/',
			})
			.success(function(response, status){
				if(status == 200){
					var response_data = {
						success: true,
						result: response
					};
				} else {
					var response_data = {
						success: false,
						result: response
					};
				}

				callback(response_data);
			})
			.error(function(response, status){
				var response_data = {
					success: false,
					result: response
				};
				callback(response_data);
			})
		}
	};

	return service;
}]);