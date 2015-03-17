DiscussApp.factory('TopicService', ['$http', '$state', 'Resources', function($http, $state, Resources){

	var service = {

		getAllTopics: function(){
			var request = $http({
				method: 'GET',
				url: Resources.SERVER_DOMAIN + '/api/topics/',
			});

			var promise = request.then(function(response){
				return response.data;
			},
			function(reason, status){
				// if(status == 403)
				// 	$state.go('login');
			});
			return promise;
		}
	};

	return service;
}]);