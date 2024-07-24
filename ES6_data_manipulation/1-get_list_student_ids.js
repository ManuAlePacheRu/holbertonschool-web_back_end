export default function getListStudentIds(studList) {
  if (!Array.isArray(studList) || studList.length === 0) {
    return [];
  }
  const idsArray = studList.map((student) => student.id);
  return idsArray;
}
