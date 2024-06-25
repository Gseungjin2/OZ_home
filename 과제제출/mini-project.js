 // Date and Time
 function updateDateTime() {
    const now = new Date();
    document.getElementById('datetime').innerHTML = `오늘 날짜와 시간: ${now.toLocaleDateString()} ${now.toLocaleTimeString()}`;
}
setInterval(updateDateTime, 1000); 
 
// Register Button Event
const registerButton = document.getElementById('register-button');
registerButton.addEventListener('click', () => {
    // Logic to open a registration form
    alert('회원가입 페이지로 이동합니다.');
    // Add navigation or form display logic here
});

// Toggle Dark Mode
const toggleThemeButton = document.getElementById('toggle-theme');
toggleThemeButton.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', newTheme);
});
