function startup() {
	swampdragon.open(function() {
    swampdragon.subscribe('notification', 'notification', null, function (context, data) {
      console.log('Successfully subscribed');
    }, function () {
      console.error('Error', arguments);
    });
  });

  swampdragon.onChannelMessage(function(channels, message) {
    if (channels.indexOf('notification') > -1) {
      if (message.action == 'created') {
        createNotificationElement(message.data.message, message.data.verb);
      }
    }
  });
}

function createNotificationElement(text, className) {
  var ul = document.getElementById('notication_list');
  var li = document.createElement('li');
  ul.appendChild(li);
  li.innerHTML = text;
  li.classList.add(className);
}