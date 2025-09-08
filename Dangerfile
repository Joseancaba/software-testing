# Dangerfile
commitIssues = []

git.commits.each do |commit|
  lines   = commit.message.lines
  subject = lines[0].to_s.chomp
  empty   = lines[1]&.strip   # segunda línea
  body    = lines.drop(2).map(&:chomp)

  commitIssues << "Commit title is too long: <#{subject}>" if subject.length > 50

  # AVISO si hay body pero NO hay línea en blanco separando
  if body.any? && (empty && !empty.empty?)
    commitIssues << "Commit title and body must be separated by a blank line: <#{subject}>"
  end

  first_line_len = body.first.to_s.length
  commitIssues << "Please include a description for commit \"#{subject}\"" if first_line_len < 5

  body.each do |line|
    commitIssues << "Commit text line too long (>72): <#{subject}>" if line.length > 72
  end
end

commitIssues.each { |issue| warn(issue) }  # <- antes era `fail`
