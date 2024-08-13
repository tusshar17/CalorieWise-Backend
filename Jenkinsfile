pipeline {
    agent any
    
    stages {
        stage("Pull Code") {
            steps {
                echo "Cloning the code"   
                git url: "https://github.com/tusshar17/CalorieWise-Backend.git", branch: "master"
            }
        }
        stage("Build") {
            steps {
                echo "Building...."
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying...."
                sh "docker compose down && docker compose up -d"
            }
        }
    }
}