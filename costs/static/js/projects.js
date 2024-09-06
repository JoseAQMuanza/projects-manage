document.addEventListener('DOMContentLoaded', function() {
  setTimeout(function() {
      var messageContainer = document.getElementById('message-container');
      if (messageContainer) {
          messageContainer.style.display = 'none';
      }
  },  3000); // 5000 milissegundos = 5 segundos
});
