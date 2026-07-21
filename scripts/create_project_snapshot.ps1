$output = "PROJECT_CONTEXT.md"

"=====================================" | Out-File $output
"IT Career Agent Project Snapshot" | Out-File $output -Append
"Generated: $(Get-Date)" | Out-File $output -Append
"=====================================" | Out-File $output -Append


"`n## Git Status" | Out-File $output -Append

git status | Out-File $output -Append


"`n## Git Log" | Out-File $output -Append

git log --oneline -10 | Out-File $output -Append


"`n## Project Structure" | Out-File $output -Append

tree /F /A | Out-File $output -Append


"`n## Python Files" | Out-File $output -Append

Get-ChildItem app -Recurse -Filter *.py |
ForEach-Object {

    "`n--------------------------------" |
    Out-File $output -Append

    $_.FullName |
    Out-File $output -Append

    Get-Content $_.FullName |
    Out-File $output -Append
}


"`n## Test Files" | Out-File $output -Append

Get-ChildItem tests -Recurse -Filter *.py |
ForEach-Object {

    "`n--------------------------------" |
    Out-File $output -Append

    $_.FullName |
    Out-File $output -Append

    Get-Content $_.FullName |
    Out-File $output -Append
}


Write-Host "Created $output"