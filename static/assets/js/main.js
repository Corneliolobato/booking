document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('roomForm');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const roomNumber = document.getElementById('roomNumber').value;
        const roomType = document.getElementById('roomType').value;
        const price = document.getElementById('price').value;
        const status = document.getElementById('status').value;

        const newRoom = await createRoom(roomNumber, roomType, price, status);
        if (newRoom) {
            // Update the UI with the new room
            const roomList = document.getElementById('roomList');
            const roomItem = document.createElement('li');
            roomItem.textContent = `Room ${newRoom.room_number} - ${newRoom.room_type} - $${newRoom.price} - ${newRoom.status}`;
            roomList.appendChild(roomItem);
        }
    });
});