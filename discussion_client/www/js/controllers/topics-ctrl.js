DiscussApp.controller('TopicsCtrl', ['$scope', 'TopicService', function($scope, TopicService){

	var ctrlData = {};

	$scope.like_topic = function(topicId){
		TopicService.likeTopic(topicId).then(function(response){
			for(var i=0; i<$scope.data.topics.length; i++){
				if($scope.data.topics[i].id == topicId){
					$scope.data.topics[i].likes_count++; 
				}
			}
		});
	}

	TopicService.getAllTopics()
	.then(function(topics){
		ctrlData.topics = topics;
		$scope.data = ctrlData;
	});
}]);