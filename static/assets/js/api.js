async function createRoom(roomNumber, roomType, price, status) {
    const response = await fetch('http://localhost:8000/api/rooms/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            room_number: roomNumber,
            room_type: roomType,
            price: price,
            status: status
        }),
    });

    if (response.status === 201) {
        const data = await response.json();
        console.log('Room created:', data);
        return data;
    } else {
        console.error('Failed to create room');
        return null;
    }
}