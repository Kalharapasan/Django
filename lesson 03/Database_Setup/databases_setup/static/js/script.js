// Highlight clicked row
document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('#student-table tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', function() {
            // Remove highlight from all rows
            rows.forEach(r => r.classList.remove('selected'));
            // Add highlight to clicked row
            this.classList.add('selected');
        });
    });
});
