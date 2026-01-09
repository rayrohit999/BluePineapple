export default function TodoList() {
    const tasks = [
        { id: 1, text: "Learn React" },
        { id: 2, text: "Practice JavaScript" },
        { id: 3, text: "Build a Todo App" },
        { id: 4, text: "Deploy node app"},
        { id: 5, text: "Complete React assignments"},
        { id: 6, text: "Learn Docker"},
        { id: 7, text: "Learn CI/CD"}
    ];

    return(
        <div>
            <ul>
                {tasks.map((task) => (
                    <li key={task.id}>{task.text}</li>
                ))}
            </ul>
        </div>
    );
}