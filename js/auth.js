// Auth related functions
const auth = {
    token: localStorage.getItem('token'),
    user: JSON.parse(localStorage.getItem('user')),

    isAuthenticated() {
        return !!this.token;
    },

    async login(email, password) {
        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error);
            }

            this.token = data.token;
            this.user = data.user;
            
            localStorage.setItem('token', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));

            return data;
        } catch (error) {
            throw error;
        }
    },

    async register(userData) {
        try {
            const response = await fetch('/api/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error);
            }

            this.token = data.token;
            this.user = data.user;
            
            localStorage.setItem('token', data.token);
            localStorage.setItem('user', JSON.stringify(data.user));

            return data;
        } catch (error) {
            throw error;
        }
    },

    async updateProfile(updates) {
        try {
            const response = await fetch('/api/auth/profile', {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                },
                body: JSON.stringify(updates)
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error);
            }

            this.user = data.user;
            localStorage.setItem('user', JSON.stringify(data.user));

            return data;
        } catch (error) {
            throw error;
        }
    },

    logout() {
        this.token = null;
        this.user = null;
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        window.location.href = '/';
    }
};

// Create login/register modal HTML
const authModal = document.createElement('div');
authModal.id = 'authModal';
authModal.innerHTML = `
    <div class="auth-modal">
        <div class="auth-tabs">
            <button class="auth-tab active" data-tab="login">Login</button>
            <button class="auth-tab" data-tab="register">Register</button>
        </div>
        
        <div class="auth-content" id="loginForm">
            <h2>Login</h2>
            <form onsubmit="return handleLogin(event)">
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        </div>

        <div class="auth-content hidden" id="registerForm">
            <h2>Register</h2>
            <form onsubmit="return handleRegister(event)">
                <input type="text" name="name" placeholder="Full Name" required>
                <input type="email" name="email" placeholder="Email" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="password" name="confirmPassword" placeholder="Confirm Password" required>
                <button type="submit">Register</button>
            </form>
        </div>
    </div>
`;

document.body.appendChild(authModal);

// Add styles
const styles = `
    .auth-modal {
        display: none;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        z-index: 1000;
        width: 90%;
        max-width: 400px;
    }

    .auth-modal.active {
        display: block;
    }

    .auth-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        z-index: 999;
    }

    .auth-overlay.active {
        display: block;
    }

    .auth-tabs {
        display: flex;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #eee;
    }

    .auth-tab {
        padding: 0.75rem 1.5rem;
        border: none;
        background: none;
        cursor: pointer;
        font-size: 1rem;
        opacity: 0.7;
        transition: all 0.3s;
    }

    .auth-tab.active {
        opacity: 1;
        border-bottom: 2px solid var(--primary);
        margin-bottom: -2px;
    }

    .auth-content {
        transition: all 0.3s;
    }

    .auth-content.hidden {
        display: none;
    }

    .auth-content form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .auth-content input {
        padding: 0.75rem 1rem;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 1rem;
    }

    .auth-content button {
        padding: 0.75rem;
        background: var(--primary);
        color: white;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.3s;
    }

    .auth-content button:hover {
        background: var(--primary-dark);
    }
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = styles;
document.head.appendChild(styleSheet);

// Add auth-related functions
async function handleLogin(event) {
    event.preventDefault();
    const form = event.target;
    
    try {
        await auth.login(
            form.email.value,
            form.password.value
        );
        closeAuthModal();
        updateAuthUI();
        // Optionally reload or update the page
        window.location.reload();
    } catch (error) {
        alert(error.message);
    }
}

async function handleRegister(event) {
    event.preventDefault();
    const form = event.target;
    
    if (form.password.value !== form.confirmPassword.value) {
        alert("Passwords don't match");
        return;
    }

    try {
        await auth.register({
            name: form.name.value,
            email: form.email.value,
            password: form.password.value
        });
        closeAuthModal();
        updateAuthUI();
        // Optionally reload or update the page
        window.location.reload();
    } catch (error) {
        alert(error.message);
    }
}

function showAuthModal(tab = 'login') {
    const modal = document.getElementById('authModal');
    const overlay = document.createElement('div');
    overlay.className = 'auth-overlay';
    document.body.appendChild(overlay);
    
    modal.querySelector(`.auth-tab[data-tab="${tab}"]`).click();
    modal.classList.add('active');
    overlay.classList.add('active');

    // Close on overlay click
    overlay.addEventListener('click', closeAuthModal);
}

function closeAuthModal() {
    const modal = document.getElementById('authModal');
    const overlay = document.querySelector('.auth-overlay');
    
    modal.classList.remove('active');
    overlay?.remove();
}

function switchAuthTab(tab) {
    const tabs = document.querySelectorAll('.auth-tab');
    const contents = document.querySelectorAll('.auth-content');
    
    tabs.forEach(t => t.classList.remove('active'));
    contents.forEach(c => c.classList.add('hidden'));
    
    document.querySelector(`.auth-tab[data-tab="${tab}"]`).classList.add('active');
    document.getElementById(`${tab}Form`).classList.remove('hidden');
}

// Add click handlers for tabs
document.querySelectorAll('.auth-tab').forEach(tab => {
    tab.addEventListener('click', () => switchAuthTab(tab.dataset.tab));
});

// Update UI based on auth state
function updateAuthUI() {
    const authButtons = document.querySelector('.auth-buttons');
    if (!authButtons) return;

    if (auth.isAuthenticated()) {
        authButtons.innerHTML = `
            <span>Welcome, ${auth.user.name}</span>
            <button onclick="handleLogout()">Logout</button>
        `;
    } else {
        authButtons.innerHTML = `
            <button onclick="showAuthModal('login')">Login</button>
            <button onclick="showAuthModal('register')">Register</button>
        `;
    }
}

function handleLogout() {
    auth.logout();
    updateAuthUI();
}

// Add auth buttons to navigation
const nav = document.querySelector('nav');
const authButtons = document.createElement('div');
authButtons.className = 'auth-buttons';
nav.appendChild(authButtons);

// Initialize UI
updateAuthUI();