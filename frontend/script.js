function addWord() {
    const word = document.getElementById("newWord").value;
    const wordList = document.getElementById("wordList");
    const listItem = document.createElement("li");
    listItem.textContent = word;
    wordList.appendChild(listItem);
    document.getElementById("newWord").value = "";
  }
  
 
const form = document.getElementById('bookingForm');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const phone = document.getElementById('phone').value;

  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, phone })
  })
  
  .then(response => response.json())
  .then(data => {
    // Обработка успешного ответа
    
    form.reset();
  })
  .catch(() => {
    
    form.reset();
  });
  alert('Форма успешно отправлена');
});


const loginForm = document.getElementById('loginForm');
const loginMessage = document.getElementById('loginMessage');

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  try {
    const response = await fetch('http://localhost:5003/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      if (response.status === 401) {
        loginMessage.textContent = 'Неверный логин или пароль';
      } else {
        const errorData = await response.json();
        loginMessage.textContent = errorData.error || 'Ошибка входа';
      }
      loginMessage.style.color = 'red';
      return;
    }

    const data = await response.json();
    loginMessage.textContent = 'Вход выполнен успешно!';
    loginMessage.style.color = 'green';

  } catch (error) {
    loginMessage.textContent = 'Такой пользователь пока что нет'
    loginMessage.style.color = 'red';
  }
});