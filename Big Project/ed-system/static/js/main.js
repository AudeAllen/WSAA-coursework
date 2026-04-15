// Utility function to show alerts
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('main');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
}

// Utility function for form validation
function validateForm(formData) {
    const requiredFields = ['first_name', 'last_name', 'dob', 'gender', 'phone', 'address'];
    
    for (let field of requiredFields) {
        if (!formData[field] || formData[field].trim() === '') {
            return { valid: false, message: `${field.replace('_', ' ').toUpperCase()} is required.` };
        }
    }
    
    return { valid: true };
}

// Disable buttons after submission to prevent double submission
function disableButton(button) {
    button.disabled = true;
    button.textContent = 'Processing...';
}

function enableButton(button, originalText) {
    button.disabled = false;
    button.textContent = originalText;
}

function formatDateTime(value) {
    if (!value) {
        return '-';
    }

    const parsedDate = new Date(value);

    if (Number.isNaN(parsedDate.getTime())) {
        return value;
    }

    return parsedDate.toLocaleString();
}

// References:
// - AI assistance: GitHub Copilot (GPT-5.3-Codex)
// - MDN JavaScript guide: https://developer.mozilla.org/docs/Web/JavaScript/Guide
// - MDN Date object: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date
// - W3Schools JavaScript tutorial: https://www.w3schools.com/js/
// - W3Schools DOM tutorial: https://www.w3schools.com/js/js_htmldom.asp
