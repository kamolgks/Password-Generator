/**
 * Function to toggle between dark and light themes.
 * It checks the current theme applied to the document body
 * and switches to the opposite theme when the button is clicked.
 * The button's text and ARIA label are also updated accordingly.
 *
 * Usage:
 * - Add this function to your script.
 * - Ensure there's a button with a 'data-theme-toggle' attribute.
 * - Define CSS classes 'dark-theme' and 'light-theme' for the respective themes.
 */

function changeTheme() {
    const body = document.body;
    const button = document.querySelector('[data-theme-toggle]');
    const currentTheme = body.classList.contains('dark-theme') ? 'dark' : 'light';

    if (currentTheme === 'dark') {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
        button.textContent = 'Dark theme';
        button.setAttribute('aria-label', 'Dark theme');
    } else {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
        button.textContent = 'Light theme';
        button.setAttribute('aria-label', 'Light theme');
    }
}