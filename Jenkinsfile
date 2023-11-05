pipeline {
    agent any

    tools {
        // Install the Maven version configured as "M3" and add it to the path.
        maven "MAVEN_HOME"
    }

    stages {
        stage('Clone') {
            steps {
                timeout(time: 2, unit: 'MINUTES'){
                    git branch: 'main', credentialsId: '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', url: 'https://github.com/Ever1ck/sysistat.git'
                }
            }
        }
        stage('Test') {
            steps {
                timeout(time: 4, unit: 'MINUTES'){
                    // Se cambia <test> por <install> para que se genere el reporte de jacoco
                    sh "python3 istat/manage.py test"
                }
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    // Ejecuta el análisis de SonarQube
                    sh 'sonar-scanner'  // Asegúrate de que 'sonar-scanner' esté instalado en tu entorno
                }
            }
        }
        /*stage('SonarQube Analysis') {
            steps { 
                withSonarQubeEnv('SonarQube Server') {
                sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=Istat2 \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://docker.sonar:9000 \
                    -Dsonar.login=admin
                    -Dsonar.password=Da12345*
                '''
                }
            }
        }*/
    }
}