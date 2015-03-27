DiscussApp.factory('TopicService', ['$http', '$state', 'Resources', function($http, $state, Resources){

	var likeDislikeTopic = function(topicId, likeStatus){
		var request = $http({
			method: 'PUT',
			url: Resources.SERVER_DOMAIN + '/api/like-topic/' + topicId + '/',
			data: {
				like: likeStatus
			}
		});

		var promise = request.then(function(response){
			return response;
		},function(response){
			return response;
		});
		return promise;
	};

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
		},

		likeTopic: function(topicId){
			return likeDislikeTopic(topicId, true).then(function(response){
				return response;
			});
		},

		dislikeTopic: function(topicId){
			return likeDislikeTopic(topicId, false).then(function(response){
				return response;
			});
		}
	};

	return service;
}]);